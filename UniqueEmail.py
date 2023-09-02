def numUniqueEmails(emails):

  res = set()

  for e in emails:
      local, domain = e.split("@")
      local = local.split("+")[0]
      local = local.replace(".", "")
      res.add((local,domain))


  return len(res)





numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])