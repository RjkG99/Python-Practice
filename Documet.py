class Document:
    def __init__(self,docId,docName,docDetails):
        self.docId = docId
        self.docName = docName 
        self.docDetails = docDetails 

class DocumentArchive:
    def __init__(self,archiveId,documentList):
        self.archiveId = archiveId
        self.documentList = documentList
    def findDateFromDocumentDetails(self):
        doclist = []
        for doc in self.documentList:
            val = doc.docDetails.split(',')
            if doc.docDetails.count('/')==2:
                for x in val:
                    if '/' in x:
                        doclist.append((doc.docId,x)) 
        return doclist
        

    def countDocumentsOfGivenType(self,docType):
        c = 0 
        for doc in self.documentList:
            type = doc.docName.split('.')[1]
            if type == docType :
               c += 1
        return c



if __name__ =="__main__":
    
    dlist = []
    n = int(input())
    for i in range(n):
        docId = int(input())
        docName = input()
        docDetails = input()
        dlist.append(Document(docId,docName,docDetails))
    doc = DocumentArchive("TCS",dlist)
    docType = input()
    ans = doc.findDateFromDocumentDetails()
    if ans != None:
        for i in ans:
            print(i[0],i[1])

    count = doc.countDocumentsOfGivenType(docType)
    print("Document Conut =" ,count)