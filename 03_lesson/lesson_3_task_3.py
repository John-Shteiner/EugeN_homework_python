from address import Address
from mailing import Mailing


to_addr = Address("123456", "Петропавловск-Камчатский", "Чкалова", "10", "5")
from_addr = Address("654321", "Новосибирск", "Садовая", "25", "12")


shipment = Mailing(to_addr, from_addr, 500, "TRK987654")


print(f"Отправление {shipment.track} из {shipment.from_address.index}, {shipment.from_address.city}, "
      f"{shipment.from_address.street}, {shipment.from_address.house} - {shipment.from_address.apartment} "
      f"в {shipment.to_address.index}, {shipment.to_address.city}, {shipment.to_address.street}, "
      f"{shipment.to_address.house} - {shipment.to_address.apartment}. "
      f"Стоимость {shipment.cost} рублей.")