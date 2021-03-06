"""Internet Group Management Protocol."""

from pypacker import pypacker, checksum


class IGMP(pypacker.Packet):
	__hdr__ = (
		("type", "B", 0),
		("maxresp", "B", 0),
		("sum", "H", 0, True),
		("group", "I", 0)
	)

	def bin(self, update_auto_fields=True):
		if update_auto_fields and self.sum_au_active and self._changed():
			self.sum = 0
			self.sum = checksum.in_cksum(pypacker.Packet.bin(self))
		return pypacker.Packet.bin(self, update_auto_fields=update_auto_fields)
