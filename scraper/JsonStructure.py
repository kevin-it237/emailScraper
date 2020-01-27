class JsonStructure():
    
    """
    author : ?????????????????????
    params : Nemails,Nsources,Enterurl,LastpageNbr
    description : tranform a data to a json form
    return : filecontent with boolean which tell if already exist or no
    """
    def JsonStructureReturn(self, Nemails, Nsources, EnterUrl, LastpageNbr):
        self.LastpageNbr = LastpageNbr
        emails = []
        AllData = []
        data = []
        EmailSources = []
        NewEmails = []
        NewEmailSources = []
        for email, source in zip(Nemails, Nsources):
            AllData.append("{} {}".format(email, source))

        output = sorted(AllData)


        for items in output:
            emails.append(items.split(" ")[0])
            EmailSources.append(items.split(" ")[1])

        index = 0
        for mail in emails:
            count = emails.count(mail)
            if mail not in NewEmails:
                NewEmails.append(mail)

                sourceWithoutDbl = []
                for counter in EmailSources[index:index + count]:
                    if counter not in sourceWithoutDbl: sourceWithoutDbl.append(counter)
                NewEmailSources.append(sourceWithoutDbl)
                index += count

        for emailsCounter in range(len(NewEmails)):
            jsonReturn = {
                "email": NewEmails[emailsCounter],
                "url": NewEmailSources[emailsCounter]
            }
            data.append(jsonReturn)

        return data