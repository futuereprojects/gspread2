def apply_font(cell):
    ws = cell._worksheet
    wb = ws._workbook
    font = cell.font

    json_data = {}
    fields = []
    if font.name is not None:
        json_data['fontFamily'] = font.name
        fields.append('userEnteredFormat.textFormat.fontFamily')
    if font.size is not None:
        json_data['fontSize'] = font.size
        fields.append('userEnteredFormat.textFormat.fontSize')
    if font.bold is not None:
        json_data['bold'] = font.bold
        fields.append('userEnteredFormat.textFormat.bold')
    if font.italic is not None:
        json_data['italic'] = font.italic
        fields.append('userEnteredFormat.textFormat.italic')
    if font.strikethrough is not None:
        json_data['strikethrough'] = font.strikethrough
        fields.append('userEnteredFormat.textFormat.strikethrough')
    if font.underline is not None:
        json_data['underline'] = font.underline
        fields.append('userEnteredFormat.textFormat.underline')
    if font.color is not None:
        color = font.color
        json_data['foregroundColor'] = {
            'red': color.red,
            'green': color.green,
            'blue': color.blue,
            'alpha': color.alpha
        }
        fields.append('userEnteredFormat.textFormat.foregroundColor')

    req_data = {'requests': [
        {
            'repeatCell': {
                'range': {
                    'sheetId': ws.id,
                    'startColumnIndex': cell.column - 1,
                    'endColumnIndex': cell.column,
                    'startRowIndex': cell.row - 1,
                    'endRowIndex': cell.row,
                },
                'cell': {
                    'userEnteredFormat': {
                        'textFormat': json_data
                    },
                },
                'fields': ', '.join(fields),
            }
        }
    ]}
    wb.batch_update(req_data)


def apply_fill(cell):
    ws = cell._worksheet
    wb = ws._workbook
    bg_color = cell.fill
    json_data = {'backgroundColor': {
        'red': bg_color.red,
        'green': bg_color.green,
        'blue': bg_color.blue,
        'alpha': bg_color.alpha,
    }}
    req_data = {'requests': [
        {
            'repeatCell': {
                'range': {
                    'sheetId': ws.id,
                    'startColumnIndex': cell.column - 1,
                    'endColumnIndex': cell.column,
                    'startRowIndex': cell.row - 1,
                    'endRowIndex': cell.row,
                },
                'cell': {
                    'userEnteredFormat': json_data,
                },
                'fields': 'userEnteredFormat.backgroundColor',
            }
        }
    ]}
    wb.batch_update(req_data)


def apply_border(cell):
    pass
