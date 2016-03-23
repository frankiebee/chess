class Game
	attr_accessor :board, :input
	def initalize
		@board = Array.new(8) {[]}
	end
	def get_move
		@input = gets.chomp.split(" ")

end


