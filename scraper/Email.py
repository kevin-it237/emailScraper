import re
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from bs4 import BeautifulSoup
from .BingSearch import BingSearch
from .Source import Source
from .JsonStructure import JsonStructure


class Email():
    """
    author : Essongo Joel Stephane
    params : FileContent
    description : give the 10 first emails
    return : 10 emails starting at the p position in the file content
    """
    def ReturnTenEmails(self, p, FileContent):
        result = []
        allEmails = FileContent[0:len(FileContent)-2]
        p = int(p)
        if len(allEmails[p:]) >= 10:
            EmailsToReturn = allEmails[p:(p+10)]
            result.append(EmailsToReturn)
            p += len(EmailsToReturn)
            result.append(p)
            result.append(True)
            return result
        else:
            EmailsToReturn = allEmails[p:]
            result.append(EmailsToReturn)
            p += len(EmailsToReturn)
            result.append(p)
            result.append(True)
            return result

    """
    author : Essongo Joel Stephane
    params : EnterUrl, p
    description : ask to Essongo 
    return:
    """
    def main(self, EnterUrl, p):
        if BingSearch.UrlValidation(BingSearch,EnterUrl) == True:
            PureUrl = BingSearch.ExtractGoodDomain(BingSearch, EnterUrl)
            urls = BingSearch.NbrPage(BingSearch, PureUrl, None,50)
            ScrapedEmail = Email.GetEmail(Email, urls,PureUrl)
            DatasStructured = JsonStructure.JsonStructureReturn(JsonStructure, ScrapedEmail[0], ScrapedEmail[1],PureUrl, urls[1])
            return DatasStructured
            # if DatasStructured == True:
            #     FileManager.__init__(FileManager)
            #     fc = FileManager.ReadFile(FileManager, PureUrl)
            #     EmailsToReturn = self.ReturnTenEmails(self, p, fc)
            #     return EmailsToReturn
            # else:
            #     return []
        else:
            # URL is not valid
            return 'YOU ENTERED A BAD URL!!'

    
    """
    author : ??????????????
    params : urls, PureURL
    description : ??????
    return:Emails And Sources
    """
    def GetEmail(self, urls,PureUrl):
        emails = []
        sources = []
        Source.__init__(Source)
        with PoolExecutor(max_workers=7) as executor:
            if type(urls[0]) == str:
                urls = urls
            else:
                urls = urls[0]

            for _ in executor.map(BingSearch.InitialSearch, urls):
                soup = BeautifulSoup(_, features="html.parser")
                lipath = soup.findAll("li", {"class": "b_algo"})
                li_number = 0
                while True:
                    try:
                        litext = lipath[li_number].text
                        # for line in the drivertextclear
                        for line in litext.splitlines():
                            # search all email in each line, return the objet searchNumbers of type list

                            SearchEmails = re.findall(r"[a-zA-Z]+[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(PureUrl),
                                                      line, flags=re.MULTILINE)
                            # for email in email_1 list

                            if SearchEmails:
                                src = Source.search(Source, li_number, lipath)
                                for email in SearchEmails:
                                    # add email in the emails list: return an object oy type NoneType
                                    emails.append(email)
                                    sources = Source.AppendSource(Source, src)
                        li_number = li_number + 1

                    except:
                        break
            EmailsAndSources = [emails, sources]
            return EmailsAndSources
