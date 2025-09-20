class Episode:
    def __init__(self, title, duration_minutes, is_played=False):
        self.title = title
        self.duration_minutes = duration_minutes
        self.is_played = is_played

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class PodcastFeedBase:
    def __init__(self):
        self.first = None
        self._size = 0

    def add_new_episode(self, episode):
        new_node = Node(episode)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def get_size(self):
        return self._size

class PodcastFeed(PodcastFeedBase):
    total_listening_time = 0

    def __init__(self):
        super().__init__()

    def mark_as_played(self, title):
        curr = self.first
        while curr:
            if curr.value.title == title and not curr.value.is_played:
                curr.value.is_played = True
                PodcastFeed.total_listening_time += curr.value.duration_minutes
                return curr.value
            curr = curr.next
        return None

    @property
    def unplayed_duration(self):
        total = 0
        curr = self.first
        while curr:
            if not curr.value.is_played:
                total += curr.value.duration_minutes
            curr = curr.next
        return total

    def archive_played_episodes(self):
        archived_count = 0
        prev, curr = None, self.first
        while curr:
            if curr.value.is_played:
                if prev is None:
                    self.first = curr.next
                    curr = self.first
                else:
                    prev.next = curr.next
                    curr = prev.next
                self._size -= 1
                archived_count += 1
            else:
                prev, curr = curr, curr.next
        return archived_count