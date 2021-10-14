import os

from .html import header, footer


class ScalpelText:
    """ This class implements the Scalpel text.
    """
    def __init__(self, text, style='p'):
        self.text = text
        self.style = style

    def __str__(self):
        if len(self.text) > 8:
            display_text = self.text[:5] + '...'
        else:
            display_text = self.text
        return f'<class "ScalpelText", style="{self.style}" text="{display_text}"'

    def to_html(self):
        return f'<{self.style}>{self.text}</{self.style}>'


class ScalpelTable:
    """ This class implements the Scalpel table.
    """
    def __init__(self, columns=None, table_class='striped', img_exts=None, img_height=128):
        self.__columns = [] if columns is None else columns
        self.table_class = table_class
        self.img_exts = ['png', 'jpg', 'jpeg'] if img_exts is None else img_exts
        self.img_height = img_height

        self.__rows = []

    def append_row(self, row):
        if len(row) != len(self.__columns):
            raise Exception(f'Number of entries in this row ({len(row)}) is not consistent with '
                            f'the number of columns ({len(self.__columns)})')
        self.__rows.append(row)

    def set_value(self, row_idx, column_name, value):
        if row_idx < 0 or row_idx >= len(self.__rows):
            raise Exception(f'Row index ({row_idx}) is smaller than 0 or larger than '
                            f'the number of rows {len(self.__rows)}')
        if column_name not in self.__columns:
            raise Exception(f'Column name ({column_name}) not in pre-defined columns')

        column_idx = self.__columns.index(column_name)
        self.__rows[row_idx][column_idx] = value

    def to_html(self):
        html = f'<table class={self.table_class}>\n'

        # thead
        html += '<thead><tr>\n'
        for col in self.__columns:
            html += f'<th>{col}</th>\n'
        html += '</tr></thead>\n'

        # tbody
        html += '<tbody>\n'
        for row in self.__rows:
            html += '<tr>'
            for v in row:
                if isinstance(v, str) and v.split('.')[-1].lower() in self.img_exts:
                    html += f'<td><img src="{v}" height="{self.img_height}"></td>'
                else:
                    html += f'<td>{v}</td>'
            html += '</tr>\n'
        html += '</tbody>\n'

        html += '</table>\n'
        return html


class ScalpelPage:
    """ This class implements the Scalpel page.
    """
    def __init__(self):
        self.__components = []

    def add_component(self, component):
        self.__components.append(component)

    def to_html(self):
        html = ''
        for comp in self.__components:
            html += comp.to_html()
        return html


class ScalpelDashboard:
    """ This class implements the Scalpel dashboard.
    """
    def __init__(self, title='Scalpel Dashboard'):
        self.title = title
        self.__pages = []
        self.__curr_page = None

    def add_component(self, component):
        if len(self.__pages) == 0:
            self.__curr_page = ScalpelPage()
            self.__pages.append(self.__curr_page)
        self.__curr_page.add_component(component)

    def add_text(self, text, style='p'):
        assert style in ['p', 'h1', 'h2', 'h3', 'h4', 'h5']
        self.add_component(ScalpelText(text, style=style))

    def nav_bar(self):
        html = '<nav class="light-blue lighten-1">\n'
        html += '<div class="nav-wrapper container">\n'
        html += f'<a href="" class="brand-logo">{self.title}</a>\n'
        html += '</div>\n'
        html += '</nav>\n'
        return html

    def to_html(self):
        html = '<!HTML><html lang="en"><head>'
        html += header
        html += f'<title>{self.title}</title>\n'
        html += '<body>\n'
        html += self.nav_bar()
        html += f'<div class="container">\n'

        for page in self.__pages:
            html += page.to_html()

        html += '</div>\n'
        html += footer
        html += '</body></html>'
        return html

    def save_html(self, html_path):
        html = self.to_html()
        with open(html_path, 'w') as fp:
            fp.write(html)
        fp.close()
