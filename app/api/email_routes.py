import os
import resend 
from flask import Blueprint, request

from app.models import connection

email_routes = Blueprint("emails", __name__)

# * SEND INVITE EMAIL

@email_routes.route("/send-invite", methods=["POST"])
def send_invite_email():
    resend.api_key = os.environ["RESEND_API_KEY"]

    params: resend.Emails.SendParams = {
      "from": "Shortlisted <mail@invitations.shortlistednetwork.com>",
      "to": ["deandre@shortlistednetwork.com"],
      "subject": "hello world",
      "html": "<strong>it works!</strong>",
    }

    email = resend.Emails.send(params)
    print(email)

    return {"message": "Invite email sent!"}, 200