# Create a class for a Note object that has:
# - attribute text for storing the notes text
# - methods to add remove and clear all text on note
# - method to count and all lines of text

class Note:
    text = 'Default Text'

    def add_text(self, text_to_add):
        self.text = self.text + text_to_add

    def clear_text(self):
        self.text = ''

    def remove_text(self, text_to_remove):
        self.text = self.text.replace(text_to_remove, '')

    def count_lines(self):
        count = len(self.text.splitlines())
        return count


if __name__ == '__main__':
    note = Note()  # create a new note instance
    print(type(note))
    print('Default instance text value:', note.text)

    note.text = 'New Text'
    print('Modified instance text value:', note.text)

    note.add_text(text_to_add="; New Note Text")
    print('After adding text:', note.text)

    note.remove_text('New')
    print('After removing text:', note.text)

    note.clear_text()
    print('After clearing all text:', note.text)

    note.add_text("First line\nSecond line")
    print('After adding multi line text:', note.text)
    print('Total line count is:', note.count_lines())
