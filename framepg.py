import random
from collections import deque

class PagingWithSwapping:
    def __init__(self):
        # --- User inputs with validation loop ---
        while True:
            try:
                self.logical_memory_size = int(input("Enter logical memory size (bytes): "))
                self.physical_memory_size = int(input("Enter physical memory size (bytes): "))
                self.PAGE_SIZE = int(input("Enter page size (bytes): "))

                if self.logical_memory_size <= 0 or self.physical_memory_size <= 0 or self.PAGE_SIZE <= 0:
                    print("Error: Memory sizes and page size must be positive integers.\n")
                    continue
                if self.PAGE_SIZE > self.physical_memory_size:
                    print("Error: Page size cannot exceed physical memory size.\n")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter integers only.\n")

        # --- Derived values ---
        self.logical_pages = self.logical_memory_size // self.PAGE_SIZE
        if self.logical_memory_size % self.PAGE_SIZE != 0:
            self.logical_pages += 1  # handle remainder bytes
        self.physical_frames = self.physical_memory_size // self.PAGE_SIZE
        self.remainder_bytes = self.logical_memory_size % self.PAGE_SIZE

        if self.physical_frames == 0:
            print("Warning: Physical memory too small to hold a single page. Simulation cannot proceed.")
            self.logical_pages = 0

        # --- Page table and loaded pages ---
        all_frames = list(range(self.physical_frames))
        random.shuffle(all_frames)

        preload_pages = min(self.logical_pages // 2, max(self.physical_frames - 1, 0))
        self.page_table = {}
        self.loaded_pages = deque()

        if preload_pages > 0:
            for page in random.sample(range(self.logical_pages), preload_pages):
                frame = all_frames.pop()
                self.page_table[page] = frame
                self.loaded_pages.append(page)

        # --- Initialization summary ---
        print(f"\nPaging Initialized:")
        print(f"Page Size: {self.PAGE_SIZE} bytes")
        print(f"Logical Pages: {self.logical_pages}, Physical Frames: {self.physical_frames}, Preloaded Pages: {preload_pages}")
        if self.remainder_bytes:
            print(f"Remaining bytes in logical memory not fitting in a page: {self.remainder_bytes}")

    def translate_address(self, logical_address):
        page_number = logical_address // self.PAGE_SIZE
        offset = logical_address % self.PAGE_SIZE

        if page_number >= self.logical_pages:
            print(f"Invalid logical address {logical_address}: exceeds logical memory size.")
            return None

        # --- Page fault handling ---
        if page_number not in self.page_table:
            used_frames = set(self.page_table.values())
            all_frames = set(range(self.physical_frames))
            free_frames = list(all_frames - used_frames)

            if free_frames:
                new_frame = free_frames[0]
                print(f"Page Fault: Loaded Page {page_number} into Frame {new_frame}")
            else:
                if not self.loaded_pages:
                    print(f"Error: No loaded pages to swap out! Cannot load Page {page_number}")
                    return None
                victim_page = self.loaded_pages.popleft()
                victim_frame = self.page_table[victim_page]
                new_frame = victim_frame
                del self.page_table[victim_page]
                print(f"Page Fault + Swap: Replaced Page {victim_page} with Page {page_number} in Frame {new_frame}")

            self.page_table[page_number] = new_frame
            self.loaded_pages.append(page_number)

        frame_number = self.page_table[page_number]
        physical_address = (frame_number * self.PAGE_SIZE) + offset

        print(f"Logical {logical_address} → Physical {physical_address} (Page {page_number}, Frame {frame_number})")
        return physical_address


# --- Example Usage ---
simulate = PagingWithSwapping()

print("\n--- Address Translation ---")
for _ in range(simulate.logical_pages * 2):
    logical_addr = (random.randint(0, simulate.logical_pages - 1) * simulate.PAGE_SIZE) \
                   + random.randint(0, simulate.PAGE_SIZE - 1)
    simulate.translate_address(logical_addr)

print("\nSimulation Complete")
