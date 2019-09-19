# If you add periods ('.') between some characters in the local name part of an
# email address, mail sent there will be forwarded to the same address without
# dots in the local name.  For example, "alice.z@leetcode.com" and
# "alicez@leetcode.com" forward to the same email address.
# (Note that this rule does not apply for domain names.)
#
# If you add a plus ('+') in the local name, everything after the first
# plus sign will be ignored. This allows certain emails to be filtered,
# for example m.y+name@email.com will be forwarded to my@email.com.
# (Again, this rule does not apply for domain names.)


class Solution:
    def numUniqueEmails(self, emails):
        if len(emails) == 0:
            return

        unique_emails = set()

        for email in emails:
            split_email = email.split("@")

            new_email = split_email[0].split("+")[0]
            new_email = new_email.replace(".", "")

            complete_email = new_email + "@" + split_email[1]
            unique_emails.add(complete_email)
        #print(unique_emails)
        return len(unique_emails)


#"testemail@leetcode.com" and "testemail@lee.tcode.com"


emails = ["test.email+al+ex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]

email = ["test.email+alex@leetcode.com"]

my_sol = Solution()
my_sol.numUniqueEmails(emails)
