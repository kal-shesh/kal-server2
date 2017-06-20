import json
import os

from Core.system_consts import PATH_SEPARATOR


PDF_ROOT = ".{delimiter}PDF".format(delimiter=PATH_SEPARATOR)

class PdfGenerator(object):
    @staticmethod
    def create_pdf(form):
        with open('data.json', 'w') as f:
            json.dump(form, f)

        pdf_path = "{pdf_root}{delimiter}Templates{delimiter}{form_type}.pdf".format(pdf_root=PDF_ROOT,
                                                                                     delimiter=PATH_SEPARATOR,
                                                                                     form_type=form.metadata.form_type)

        pdf_output_path = "{pdf_root}{delimiter}OutputFolder{delimiter}{form_type}_out.pdf".format(pdf_root=PDF_ROOT,
                                                                                                   delimiter=PATH_SEPARATOR,
                                                                                                   form_type=form.metadata.form_type)

        cmd = "{pdf_root}{delimiter}Templates{delimiter}PdfFiller.exe {pdfPath} {pdfOutputPath} {data}"\
            .format(pdf_root=PDF_ROOT,
                    delimiter=PATH_SEPARATOR,
                    pdfPath=pdf_path,
                    pdfOutputPath=pdf_output_path,
                    data='data.json')
        os.system(cmd)


