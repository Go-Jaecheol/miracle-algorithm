def solution(book_time):
    times, rooms = [], []
    for start, end in book_time:
        split_start = start.split(':')
        split_end = end.split(':')
        times.append([int(split_start[0]) * 60 + int(split_start[1]), int(split_end[0]) * 60 + int(split_end[1])])
    times.sort(key=lambda x:x[1])
    for start, end in times:
        check = False
        rooms.sort(reverse=True)
        for i, room in enumerate(rooms):
            if room <= start:
                check = True
                rooms[i] = end + 10
                break
        if not check:
            rooms.append(end + 10)
    return len(rooms)
