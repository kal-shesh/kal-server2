import json
import os
from Core import Form
from Core.system_consts import PATH_SEPARATOR

PDF_ROOT = ".{delimiter}PDF".format(delimiter=PATH_SEPARATOR)


class PdfGenerator(object):
    @staticmethod
    def create_pdf(form):
        with open(os.path.abspath("{pdf_root}{delimiter}data.json".format(pdf_root=PDF_ROOT, delimiter=PATH_SEPARATOR)),
                  'w+') as f:
            f.write(json.dumps(form.data))

        pdf_path = os.path.abspath("{pdf_root}{delimiter}Templates{delimiter}{form_type}.pdf".format(pdf_root=PDF_ROOT,
                                                                                                     delimiter=PATH_SEPARATOR,
                                                                                                     form_type=form.metadata.id))

        pdf_output_path = os.path.abspath(
            "{pdf_root}{delimiter}OutputFolder{delimiter}{form_type}.pdf".format(pdf_root=PDF_ROOT,
                                                                                     delimiter=PATH_SEPARATOR,
                                                                                     form_type=form.uuid))

        cmd = "{pdf_root}{delimiter}Templates{delimiter}PdfFiller.exe {pdfPath} {pdfOutputPath} {data}" \
            .format(pdf_root=PDF_ROOT,
                    delimiter=PATH_SEPARATOR,
                    pdfPath=pdf_path,
                    pdfOutputPath=pdf_output_path,
                    data='C:\Users\Kfiry\Documents\kal-server2\PDF\data.json')
        print cmd
        os.system(cmd)
