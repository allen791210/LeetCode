"""
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""
class Solution:
    def reorderLogFiles(self, logs):
        if not logs:
            return None

        letter_logs = []
        digit_logs = []

        for log in logs:
            string = log.split(" ")
            if string[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        letter_logs.sort(key=lambda log: (log.split()[1:], log.split()[0])) # KEY = lambda log: log.split()[1]

        return letter_logs + digit_logs