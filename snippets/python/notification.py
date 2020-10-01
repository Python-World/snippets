#Title: Notification Processor	
#Tags:plyer,python

#Can process notification of your choice 

#plyer:built in module help you to find more information


from plyer import notification

def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='Write your icon address here',
        timeout=5
    )

notifyme("Title of notification box", "Message in notification")
