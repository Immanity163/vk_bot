import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def sender(id, text):
    vk.messages.send(user_id=id, message=text, random_id=0)

vk_session = vk_api.VkApi(token="vk1.a.9FpJkaxOofCamfTGnjn7ISOPOyrO0PpNL8gJl3oFczEC4BxrG10oSdGlHpi0b1NRd4DqcwiNiqDLLLLuwgPeL1i9_q8Ii3oRqYD40bUoxB9tdCqmhDik8oHvkFAZ_535WqAV3A1HNCg-8Z-5-sWjte9UT6IEqpqj9VF-dtt9ONGWCBtCyzGFcBLCKwSvB0zX4wlCm6XmUvLu2zhdqH59og")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id

            if msg:
                sender(id,msg)