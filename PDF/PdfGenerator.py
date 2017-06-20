import json
pdfsPath = ''

class PdfGenerator():
    def CreatePdf(self,form):
        pass
    def CreateMapping(form):
        file = open('data.json','w')
        json.dumps(form,file)
        file.close()
        pdfFromPath = pdfsPath + orm.metadata.form_type +'.pdf'
        pdfOutPath = pdfsPath + orm.metadata.form_type +'_out.pdf'
        cmd = pdfsPath+'PdfFiller.exe '+pdfFromPath +' ' +pdfOutPath + ' ' + 'data.json';
        os.system(cmd)


