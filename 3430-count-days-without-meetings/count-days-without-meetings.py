class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        '''
        lets optimise this ->
        sort this based on the meeting start 
        merge the intervals if there's an overlap
        '''

        meetings.sort(key=lambda x: x[0])
        merged = []

        for meeting in meetings:
            meeting_start, meeting_end = meeting
            if not merged or merged[-1][1] < meeting_start:
                merged.append(meeting)
            else:
                merged[-1][1] = max(merged[-1][1], meeting_end)

        total_days = 0

        for meeting in merged:
            meeting_start, meeting_end = meeting
            total_days += (meeting_end - meeting_start + 1)

        return days - total_days

        

        # Dumbest solution -> Vibe Coding lol
        # meetings.sort(key=lambda x: x[0])
        # meet = [False] * (days + 1)
        # print("meet : ", meetings)

        # for m in meetings:
        #     m_start, m_end = m
        #     for i in range(m_start, m_end + 1):
        #         meet[i] = True

        # print("meet -> ", meet)
        # count = 0
        # for i in range(1, days+1):
        #     if meet[i] == False:
        #         count += 1
        # print("count => ", count)