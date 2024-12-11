from address import Address
from mailling import Mailing

mailling = Mailing("to_address", "from_address", "cost", "track")
mailling.to_address = Address("12345", "Москва", "ул. Пушкина", "10", "30")
mailling.from_address = Address("56748", "Пермь", "ул. Ленина", "21", "45")
mailling.track = "FGT333"
mailling.cost = 1500

print(f"Отправление {mailling.track} из {mailling.from_address.index}, {mailling.from_address.city}, {mailling.from_address.street}, {mailling.from_address.house}-{mailling.from_address.room} в {mailling.to_address.index}, {mailling.to_address.city}, {mailling.to_address.street}, {mailling.to_address.house}-{mailling.to_address.room}. Стоимость {mailling.cost} рублей.")
