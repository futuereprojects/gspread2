from . import colors
import warnings


__all__ = ['apply_formatting', 'apply_border']


def apply_formatting(worksheet, cells):
    wb = worksheet._workbook
    requests = []
    for cell in cells:
        if cell._font_modified is True:
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
            requests.append({
                'repeatCell': {
                    'range': {
                        'sheetId': worksheet.id,
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
            })
        if cell._fill_modified is True:
            bg_color = cell.fill
            json_data = {'backgroundColor': {
                'red': bg_color.red,
                'green': bg_color.green,
                'blue': bg_color.blue,
                'alpha': bg_color.alpha,
            }}
            requests.append({
                'repeatCell': {
                    'range': {
                        'sheetId': worksheet.id,
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
            })
    wb.batch_update({'requests': requests})


def apply_font(worksheet, cells):
    """Depreciated. Use `apply_formatting()` instead."""
    warnings.warn('This function is depreciated. Use `gspread2.styles.api.apply_formatting()` instead.')
    requests = []
    wb = worksheet._workbook
    for cell in cells:
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
        requests.append({
            'repeatCell': {
                'range': {
                    'sheetId': worksheet.id,
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
        })

    req_data = {'requests': requests}
    wb.batch_update(req_data)


def apply_fill(cell):
    """Depreciated. Use `apply_formatting()` instead."""
    warnings.warn('This function is depreciated. Use `gspread2.styles.api.apply_formatting()` instead.')
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


def apply_border(worksheet, start_row, end_row, start_column, end_column, border):
    wb = worksheet._workbook
    data = {
        'updateBorders': {
            'range': {
                'sheetId': worksheet.id,
                'startRowIndex': start_row - 1,
                'endRowIndex': end_row,
                'startColumnIndex': start_column - 1,
                'endColumnIndex': end_column,
            }
        }
    }
    for side in ('left', 'right', 'top', 'bottom'):
        border_side = getattr(border, side)
        if border_side is not None:
            border_color = colors.Color(border_side.color)
            data['updateBorders'][side] = {
                'style': border_side.border_style,
                'width': border_side.width,
                'color': {
                    'red': border_color.red,
                    'blue': border_color.blue,
                    'green': border_color.green,
                    'alpha': border_color.alpha,
                }
            }
    req_data = {'requests': [data]}
    wb.batch_update(req_data)
