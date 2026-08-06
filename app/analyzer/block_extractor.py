from app.models.block import Block


class BlockExtractor:

    def extract(self, page_number, layout):

        blocks = []

        block_id = 1

        for block in layout["blocks"]:

            if block["type"] != 0:
                continue

            font = None

            font_size = None

            parts = []

            for line in block["lines"]:

                for span in line["spans"]:

                    parts.append(span["text"])

                    if font is None:
                        font = span["font"]

                        font_size = span["size"]

                parts.append("\n")

            text = "".join(parts).strip()

            if not text:
                continue

            blocks.append(

                Block(

                    id=block_id,

                    page_number=page_number,

                    block_number=block["number"],

                    block_type="text",

                    bbox=block["bbox"],

                    text=text,

                    font=font,

                    font_size=font_size

                )

            )

            block_id += 1

        return blocks