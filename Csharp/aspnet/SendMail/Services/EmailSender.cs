using MailKit.Net.Smtp;
using Microsoft.AspNetCore.Identity.UI.Services;
using MimeKit;
using SendGrid;
using SendGrid.Helpers.Mail;

namespace WebApplication1.Services
{
    public class EmailSender : IEmailSender
    {
        const string EmailFrom = "email";
        public Task SendEmailAsync(string email, string subject, string htmlMessage)
        {
            //var emailToSend = new MimeMessage();
            //emailToSend.From.Add(MailboxAddress.Parse(EmailFrom));
            //emailToSend.To.Add(MailboxAddress.Parse(email));
            //emailToSend.Subject = subject;
            //emailToSend.Body = new TextPart(MimeKit.Text.TextFormat.Html) { Text = htmlMessage };

            //using (var emailClient = new SmtpClient())
            //{
            //    emailClient.Connect("serwer", 465, MailKit.Security.SecureSocketOptions.StartTls);
            //    emailClient.Authenticate(EmailFrom, "haslo");
            //    emailClient.Send(emailToSend);
            //    emailClient.Disconnect(true);
            //}
            //return Task.CompletedTask;
            var client = new SendGridClient("token");
            var from = new EmailAddress("from@mail.com", "Display name");
            var to = new EmailAddress(email);
            var msg = MailHelper.CreateSingleEmail(from, to, subject, "", htmlMessage);
            return client.SendEmailAsync(msg);
        }
    }
}
