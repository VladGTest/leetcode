class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        total_beams = 0
        prev_devices = 0
        for row in bank:
            curr_devices = row.count("1")
            if curr_devices > 0:
                total_beams += prev_devices * curr_devices
                prev_devices = curr_devices
        return total_beams
        