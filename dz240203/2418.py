class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # start_heights = heights
        # sort_heights = sorted(heights)
        h_name = []
        zipped_values = zip(names, heights)
        for name,height in zipped_values:
            h_name.append((height,name))
        h_name.sort()
        h_name = h_name[::-1]
        sort_people = []
        for height,name in h_name:
            sort_people.append(name)
        return sort_people