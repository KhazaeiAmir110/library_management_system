from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from apps.company.models import Company, SansConfig, SansHistoryDate, HolidaysDate, Reservation
from apps.users.models import User
from base import secret

router = APIRouter(
    prefix="/company",
    tags=["Company"]
)


@router.get("/")
async def home():
    return {"message": "Hello World"}


# # صفحه اصلی شرکت‌ها
# @router.get("/", response_class=HTMLResponse)
# async def home():
#     companies = Company.objects.filter(is_active=1)
#     join_table = Company.objects.inner_join(join_table=User, join_condition="company.user_id=user.id")
#
#     template = Template(open("templates/company/page1.html").read())
#     return HTMLResponse(template.render(companies=companies, join_table=join_table))
#
#
# # صفحه جزئیات شرکت
# @router.get("/{company_slug}", response_class=HTMLResponse)
# async def company_detail(company_slug: str):
#     company = Company.objects.get(slug=company_slug)
#
#     if company:
#         holidays = HolidaysDate.objects.filter(company_id=company[0])
#         sansconfig = SansConfig.objects.get(company_id=company[0])
#         sansholidaydatetime = SansHistoryDate.objects.get(company_id=company[0])
#         reservations = Reservation.objects.filter(company_id=company[0])
#     else:
#         holidays = "No holidays"
#         sansconfig = "No sansconfig"
#         sansholidaydatetime = "No sansholidaydatetime"
#         reservations = "No reservations"
#
#     template = Template(open("templates/company/page2.html").read())
#     return HTMLResponse(template.render(
#         company=company,
#         holidays=holidays,
#         sansconfig=sansconfig,
#         sansholidaydatetime=sansholidaydatetime,
#         reservations=reservations
#     ))
#
#
# # ارسال کد به شماره کاربر
# @router.post("/baraato/send")
# async def send_code(
#         name: str = Form(...), family: str = Form(...), number: str = Form(...),
#         email: str = Form(...), time: str = Form(...), date: str = Form(...),
#         amount: float = Form(...)
# ):
#     # ذخیره اطلاعات کاربر در session-like dictionary
#     session = {
#         "name": name,
#         "family": family,
#         "number": number,
#         "email": email,
#         "time": time,
#         "date": date,
#         "amount": amount
#     }
#
#     # ارسال پیامک به کاربر
#     api = IPPanelClient(secret.API_KEY)
#     api.send(
#         sender=secret.sender,
#         recipients=[number],
#         message=f"کد تأیید : {secret.code}\n سیستم رزرواسیون و نوبت دهی براتو",
#         summary=secret.summary
#     )
#
#     return {"status": "success"}
#
#
# # صفحه پرداخت
# @router.post("/{company_slug}/payment", response_class=HTMLResponse)
# async def payment(company_slug: str):
#     client = sudsClient(secret.ZARINPAL_WEBSERVICE)
#     amount = session.get("amount")
#
#     if not amount:
#         return HTMLResponse("Error: Amount is missing", status_code=400)
#
#     result = client.service.PaymentRequest(
#         secret.MERCHANT, amount, secret.description, secret.email, secret.phone,
#         f"http://127.0.0.1:8000/company/{company_slug}/payment/verify/"
#     )
#
#     if result.Status == 100:
#         return RedirectResponse(f"{secret.ZP_API_STARTPAY}{result.Authority}")
#     else:
#         return HTMLResponse("Error: Payment request failed", status_code=400)
#
#
# # تأیید پرداخت
# @router.get("/{company_slug}/payment/verify/", response_class=HTMLResponse)
# async def verify(company_slug: str, status: str, authority: str):
#     client = sudsClient(secret.ZARINPAL_WEBSERVICE)
#
#     if status == "OK":
#         result = client.service.PaymentVerification(secret.MERCHANT, authority, session.get("amount"))
#
#         if result.Status == 100:
#             Reservation.objects.insert(
#                 first_name=session["name"],
#                 last_name=session["family"],
#                 phone_number=session["number"],
#                 email=session["email"],
#                 date=session["date"],
#                 time=session["time"],
#                 company_id=Company.objects.get(slug=company_slug)[0]
#             )
#             template = Template(open("templates/company/page5.html").read())
#             return HTMLResponse(template.render())
#         else:
#             return HTMLResponse(f"Transaction failed. Status: {result.Status}", status_code=400)
#
#     return HTMLResponse("Transaction failed or canceled by user", status_code=400)
