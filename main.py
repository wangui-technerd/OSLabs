class PagingSimulation:
    def __init__(self, page_size=128):
        self.PAGE_SIZE = page_size
        # Page Table: {Page Number (p): Frame Number (f)}
        self.page_table = {
            0: 10,
            3: 15,  # Page 3 is in Frame 15
            7: 22,
            10: 4,
        }

    def translate_address(self, logical_address):
        page_number = logical_address // self.PAGE_SIZE
        offset = logical_address % self.PAGE_SIZE

        if page_number not in self.page_table:
            print(f"Page Fault: Page {page_number} not in memory.")
            return None

        frame_number = self.page_table[page_number]
        physical_address = (frame_number * self.PAGE_SIZE) + offset

        print(f"\nLogical Address: {logical_address}")
        print(f"Page Number: {page_number}, Offset: {offset}")
        print(f"Frame Number: {frame_number}")
        print(f"Physical Address: {physical_address}")

        return physical_address


simulate = PagingSimulation()

# Offset 70
logical_address = (3 * 128) + 70
simulate.translate_address(logical_address)
