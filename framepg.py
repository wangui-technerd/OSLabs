import random

class SimplePagingSimulation:
    def __init__(self, logical_memory_size=2048, page_size=256):
        self.PAGE_SIZE = page_size
        self.logical_pages = logical_memory_size // page_size

        # Let user define number of physical frames
        self.physical_frames = int(input("Enter number of physical frames available: "))
        if self.physical_frames <= 0:
            print("Invalid input! Defaulting to 8 frames.")
            self.physical_frames = 8

        # Create frames and randomize
        all_frames = list(range(self.physical_frames))
        random.shuffle(all_frames)

        # Preload half the logical pages
        preload_pages = min(self.logical_pages // 2, self.physical_frames)
        self.page_table = {page: all_frames[page] for page in range(preload_pages)}

        print(f"\nPaging System Initialized")
        print(f"Page Size: {self.PAGE_SIZE} bytes")
        print(f"Logical Pages: {self.logical_pages}")
        print(f"Physical Frames: {self.physical_frames}")
        print(f"Initial Page Table: {self.page_table}")

    def translate_address(self, logical_address):
        page_number = logical_address // self.PAGE_SIZE
        offset = logical_address % self.PAGE_SIZE

        print(f"\nLogical Address: {logical_address}")
        print(f"Page Number: {page_number}, Offset: {offset}")

        if page_number >= self.logical_pages:
            print(" Invalid address: exceeds logical memory size.")
            return None

        # Handle page fault
        if page_number not in self.page_table:
            print(f" Page Fault: Page {page_number} not in memory.")
            used_frames = set(self.page_table.values())
            all_frames = set(range(self.physical_frames))
            free_frames = list(all_frames - used_frames)

            if free_frames:
                new_frame = free_frames[0]
                self.page_table[page_number] = new_frame
                print(f" Loaded Page {page_number} into Frame {new_frame}. Page Table Updated.")
            else:
                print(" No free frames available — cannot load page.")
                return None

        frame_number = self.page_table[page_number]
        physical_address = (frame_number * self.PAGE_SIZE) + offset

        print(f"Frame Number: {frame_number}")
        print(f"Physical Address: {physical_address}")
        return physical_address


# --- Run Simulation ---
simulate = SimplePagingSimulation()

logical_address = (3 * simulate.PAGE_SIZE) + 70
simulate.translate_address(logical_address)

user_input = int(input("\nEnter a logical address to translate: "))
simulate.translate_address(user_input)
