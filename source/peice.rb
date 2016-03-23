class Peice
	attr_accessor :curent_space,
	attr_reader :peice_color
	def initalize(color,starting_point)
		@peice_color = color
		@starting_point = starting_point
	end

end