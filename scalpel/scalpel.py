import os

from .html import bootstrap_header, bootstrap_footer


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
        return f'<{self.style} class="mt-5">{self.text}</{self.style}>'


class ScalpelTable:
    """ This class implements the Scalpel table.
    """
    def __init__(self, columns=None, table_class='table-hover', img_exts=None, img_height=128):
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
        html = f'<table class="table {self.table_class}">\n'

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
    def __init__(self, title):
        self.title = title
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
        self.header = bootstrap_header
        self.footer = bootstrap_footer

    def add_component(self, component):
        if len(self.__pages) == 0:
            self.__curr_page = ScalpelPage(title='main')
            self.__pages.append(self.__curr_page)
        self.__curr_page.add_component(component)

    def add_text(self, text, style='p'):
        assert style in ['p', 'h1', 'h2', 'h3', 'h4', 'h5']
        self.add_component(ScalpelText(text, style=style))

    def nav_bar(self):
        html = '<header>\n'
        html += '<nav class="navbar navbar-expand-lg navbar-dark fixed-top bg-primary shadow">\n'
        html += '<div class="container">\n'
        html += f'<a class="navbar-brand" href="">{self.title}</a>\n'
        html += '<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">'
        html += '<span class="navbar-toggler-icon"></span>'
        html += '</button>\n'
        html += '<div class="collapse navbar-collapse" id="navbarCollapse">\n'
        html += '<ul class="navbar-nav mr-auto">\n'
        for i, page in enumerate(self.__pages):
            html += '<li class="nav-item">'
            if i == 0:
                html += f'<a class="nav-link active" href="#">{page.title}</a>'
            else:
                html += f'<a class="nav-link" href="#">{page.title}</a>'
            html += '</li>\n'
        html += '</div>\n'
        html += '</div>\n'
        html += '</nav>\n'
        html += '</header>\n'
        return html

    def to_html(self):
        html = '<!HTML><html lang="en"><head>'
        html += self.header
        html += f'<title>{self.title}</title>\n'
        html += '<body>\n'
        html += self.nav_bar()
        html += '<main role="main" class="container">'

        for page in self.__pages:
            html += page.to_html()

        html += '</main>\n'
        html += self.footer
        html += '</body></html>'
        return html

    def save_html(self, html_path):
        html = self.to_html()
        with open(html_path, 'w') as fp:
            fp.write(html)
        fp.close()
