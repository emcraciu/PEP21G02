# try:
#     1/0
#     raise AttributeError
#     raise Exception
# except ZeroDivisionError:
#     print('you should not divide by 0')
# except Exception:
#     print('This is a general exception')
# except AttributeError:
#     print('This is not possible')


# classes
class Note:
    text = 'Default text'

    def add_text(self):
        self.text = self.text + ' New text entry '

    def clear_text(self):
        self.text = ''

    def remove_text(self, text_to_remove):
        self.text = self.text.replace(text_to_remove, '')



note = Note().clear_text()
print(type(note))
print(type(''))

print('instance value: ', note.text)

note.text = 'new text'
print('instance value: ', note.text)

note.add_text()
print('instance value: ', note.text)

note.remove_text('New')
print('instance value: ', note.text)

note.clear_text()
print('instance value: ', note.text)

