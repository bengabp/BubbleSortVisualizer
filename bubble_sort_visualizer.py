from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivymd.app import MDApp

import random
import time
import threading

Window.size = (700, 500)

class Block(Button):
	def __init__(self, **kwargs):
		super(Block, self).__init__(**kwargs)
		self.size_hint = (None, None)
		self.width = 30
		self.bold = True


class BubbleSortAlgorithmVisualizer(MDApp):
	"""
	Bubble Sort Algorithm Visualizer made uisng KivyMD
	"""
	algo_input = []

	def __init__(self, **kwargs):
		self.iterations = 0
		self.i = 0
		self.sort_speed = 0.001
		super(BubbleSortAlgorithmVisualizer, self).__init__(**kwargs)

	def build(self):
		self.theme_cls.theme_style = "Dark"
		return Builder.load_file("design.kv")

	def bubble_sort(self, button, elements_label, widget):
		Clock.schedule_interval(self.do_sort, self.sort_speed)

	def do_sort(self, dt):
		""" Implementation of the bubble sort algorithm """

		max_iter = len(self.algo_input) ** 2
		if self.i < max_iter:
			j = self.i % (len(self.algo_input) - 1)
			self.iterations += 1
			if self.algo_input[j] > self.algo_input[j + 1]:
				self.algo_input[j], self.algo_input[j + 1] = self.algo_input[j + 1], self.algo_input[j]
			self.root.ids.elements_label.text = f"Elements = {self.algo_input}"
			self.root.ids.visualization_plane.clear_widgets()
			for n in self.algo_input:
				new_block = Block()
				new_block.height = n * 5
				new_block.text = str(n)
				self.root.ids.visualization_plane.add_widget(new_block)
			self.i += 1
		else:
			Clock.unschedule(self.do_sort)
			self.iterations = 0
			self.i = 0

	def add_random_block(self, button, elements_label, widget):
		if len(self.algo_input) <= 15:
			random_number = random.randint(10, 50)
			self.algo_input.append(random_number)
			elements_label.text = f"Elements = {self.algo_input}"
			new_block = Block()
			new_block.height = random_number * 5
			new_block.text = f"{random_number}"
			widget.add_widget(new_block)
		else:
			button.disabled = True

	def clear_blocks(self, button, elements_label, widget):
		self.algo_input.clear()
		widget.clear_widgets()
		elements_label.text = "No Elements to sort"
		self.root.ids.add_block_btn.disabled = False


if __name__ == "__main__":
	algovisualizer = BubbleSortAlgorithmVisualizer()
	algovisualizer.run()
