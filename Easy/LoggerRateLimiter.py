# #Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).
#
# All messages will come in chronological order. Several messages may arrive at the same timestamp.
#
# Implement the Logger class:
#
# Logger() Initializes the logger object.
# bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.message_dict = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.message_dict:
            new_time = timestamp + 10
            self.message_dict[message] = new_time
            return True

        print_time = self.message_dict[message]
        if print_time > timestamp:
            return False

        self.message_dict[message] = timestamp + 10
        return True


my_logger = Logger()
#
# actions = [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
# for action in actions:
#     time = action[0]
#     msg = action[1]
#     print(my_logger.shouldPrintMessage(time, msg))
# #true, true, false, false, false, true


actions = [[0,"A1"],[3,"A4"],[6,"A0"],[9,"A3"],[12,"A3"],[15,"A4"],[18,"A3"],[21,"A2"],
 [24,"A1"],[27,"A2"],[30,"A0"],[33,"A0"]]
for action in actions:
    time = action[0]
    msg = action[1]
    print(my_logger.shouldPrintMessage(time, msg), sep="")
#[true,true,true,true,false,true,false,true,true,false,true,false]
