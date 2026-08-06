import fitz
import os


class PageRenderer:

    def __init__(self, document):
        self.document = document

    def render_pages(self, output_folder="data/images", dpi=300):

        os.makedirs(output_folder, exist_ok=True)

        pdf = fitz.open(self.document.file_name)

        zoom = dpi / 72

        matrix = fitz.Matrix(zoom, zoom)

        image_paths = []

        for i, page in enumerate(pdf):

            pix = page.get_pixmap(matrix=matrix)

            path = os.path.join(
                output_folder,
                f"page_{i+1}.png"
            )

            pix.save(path)

            image_paths.append(path)

        pdf.close()

        for page_obj, image_path in zip(self.document.pages, image_paths):
            page_obj.image_path = image_path

        return self.document