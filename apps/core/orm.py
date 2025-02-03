class ORMMixin:
    def get(self, *args, **kwargs):
        keys = [key for key in kwargs]
        if len(keys) == 0:
            return None
        elif len(keys) > 1:
            return ValueError("ERROR : Users More than one")
        else:
            with self:
                results = self.execute_raw(
                    f"""
                        SELECT * FROM {self.__class__.__name__.split('Manager')[0].lower()} where
                         {keys[0]} = '{kwargs[keys[0]]}';
                    """
                )
                if len(results) == 0:
                    return None
                return results[0]

    def all(self, *args, **kwargs):
        with self:
            query = f"SELECT * FROM {self.__class__.__name__.split('Manager')[0].lower()}"
            if kwargs:
                filters = [f"{key} = '{value}'" for key, value in kwargs.items()]
                query += " WHERE " + " AND ".join(filters)

            results = self.execute_raw(query)
            if len(results) == 0:
                return None
            return results

    def update(self, *args, **kwargs):
        if not kwargs:
            raise ValueError("ERROR: No fields provided for update")

        filters = {key: kwargs.pop(key) for key in list(kwargs.keys()) if key in self.primary_keys}

        if not filters:
            raise ValueError("ERROR: No valid primary key provided for update")

        set_values = []
        for key, value in kwargs.items():
            if value is None:
                set_values.append(f"{key} = NULL")
            elif isinstance(value, str):
                set_values.append(f"{key} = '{value}'")
            else:
                set_values.append(f"{key} = {value}")

        where_clause = " AND ".join([f"{key} = '{value}'" for key, value in filters.items()])

        with self:
            self.execute_raw(
                f"""
                    UPDATE {self.__class__.__name__.split('Manager')[0].lower()}
                    SET {', '.join(set_values)}
                    WHERE {where_clause};
                """
            )
            return True

    def delete(self, *args, **kwargs):
        global key_, value_
        getting = self.get(*args, **kwargs)

        if type(getting) is tuple:
            for key, value in kwargs.items():
                key_ = key
                value_ = value
            with self:
                self.execute_raw(
                    f"""
                                    DELETE FROM {self.__class__.__name__.split('Manager')[0].lower()} WHERE
                                     {key_}='{value_}';
                                """
                )
                return True
        else:
            raise ValueError("ERROR :Not delete")

    def create(self, *args, **kwargs):
        keys = kwargs.keys()
        values = kwargs.values()

        formatted_values = []
        for value in values:
            if isinstance(value, str):
                formatted_values.append(f"'{value}'")
            elif isinstance(value, int):
                formatted_values.append(str(value))
            else:
                # Handle other types if necessary, like float, datetime, etc.
                formatted_values.append(f"'{value}'")

        with self:
            self.execute_raw(
                f"""
                    INSERT INTO {self.__class__.__name__.split('Manager')[0].lower()}
                     ({', '.join(keys)})
                     VALUES ({', '.join(formatted_values)})
                """
            )
            return True

    def filter(self, *args, **kwargs):
        keys = [key for key in kwargs]
        if len(keys) == 0:
            return None
        else:
            with self:
                results = self.execute_raw(
                    f"""
                        SELECT * FROM {self.__class__.__name__.split('Manager')[0].lower()} where
                         {keys[0]} = '{kwargs[keys[0]]}';
                    """
                )
                if len(results) == 0:
                    return None
                return results

    def inner_join(self, join_table, join_condition, *args, **kwargs):
        keys = kwargs.keys()

        with self:
            result = self.execute_raw(
                f"""
                    SELECT * FROM {self.__class__.__name__.split('Manager')[0].lower()}
                     INNER JOIN {join_table.__name__.lower()} ON {join_condition};
                """
            )
            return result
