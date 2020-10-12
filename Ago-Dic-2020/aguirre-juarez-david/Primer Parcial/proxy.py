from abc import ABC, abstractmethod

class User:
	def __init__(self, **kargs):
		self.name = kargs.get("name", "")
		self.access_level = kargs.get("access_level", 1)

class ISystemAuth(ABC):
	@abstractmethod
	def level_1_tasks(self):
		pass

	@abstractmethod
	def level_2_tasks(self):
		pass

	@abstractmethod
	def level_3_tasks(self):
		pass

class SystemAuthPayments(ISystemAuth):
	def __init__(self, user):
		self.__user = user

	def level_1_tasks(self):
		if self.__user.access_level < 1:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-1 tasks"

		return f"User '{self.__user.name}' is doing level-1 tasks on system ### Payments ###"

	def level_2_tasks(self):
		if self.__user.access_level < 2:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-2 tasks"

		return f"User '{self.__user.name}' is doing level-2 tasks on system ### Payments ###"

	def level_3_tasks(self):
		if self.__user.access_level < 3:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-3 tasks"

		return f"User '{self.__user.name}' is doing level-3 tasks on system ### Payments ###"


class SystemAuthIT(ISystemAuth):
	def __init__(self, user):
		self.__user = user

	def level_1_tasks(self):
		if self.__user.access_level < 1:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-1 tasks"

		return f"User '{self.__user.name}' is doing level-1 tasks on system ### IT ###"

	def level_2_tasks(self):
		if self.__user.access_level < 2:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-2 tasks"

		return f"User '{self.__user.name}' is doing level-2 tasks on system ### IT ###"

	def level_3_tasks(self):
		if self.__user.access_level < 3:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-3 tasks"

		return f"User '{self.__user.name}' is doing level-3 tasks on system ### IT ###"

class SystemAuthSales(ISystemAuth):
	def __init__(self, user):
		self.__user = user

	def level_1_tasks(self):
		if self.__user.access_level < 1:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-1 tasks"

		return f"User '{self.__user.name}' is doing level-1 tasks on system ### Sales ###"

	def level_2_tasks(self):
		if self.__user.access_level < 2:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-2 tasks"

		return f"User '{self.__user.name}' is doing level-2 tasks on system ### Sales ###"

	def level_3_tasks(self):
		if self.__user.access_level < 3:
			return f"ERROR: User '{self.__user.name}' is not authorized to do level-3 tasks"

		return f"User '{self.__user.name}' is doing level-3 tasks on system ### Sales ###"

class SystemAuthProxy(ISystemAuth):
	def __init__(self, user, area):
		auth_name = f"SystemAuth{area}"

		if not auth_name in [m.__name__ for m in ISystemAuth.__subclasses__()]:
			raise ValueError("Invalid area name.")

		self.__auth_area = eval(auth_name)(user)
		self.__user = user

	def level_1_tasks(self):
		return self.__auth_area.level_1_tasks()

	def level_2_tasks(self):
		return self.__auth_area.level_2_tasks()

	def level_3_tasks(self):
		return self.__auth_area.level_3_tasks()