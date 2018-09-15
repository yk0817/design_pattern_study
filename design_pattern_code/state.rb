# 良いプログラムなのでメモ
# http://qiita.com/hikao/items/e29c08d3a82bc0827a62

class State
  def ice_break
    raise "not implemented error"
  end
  
  def choose_fashion
    raise "not implemented error"
  end
end

class SunnyDay < State
  def ice_break
    puts "今日は晴れて良い天気"
  end
  def choose_fashion
    puts "なのでスニーカーを履こう"
  end
end

class RainyDay < State
  def ice_break
    puts "今日は雨がザーザー"
  end
  
  def choose_fashion
    puts "なので長靴を履こう"
  end
end

class CloudyDay < State
  def ice_break
    puts "今日は天気わるいんですかねー"
  end
  def choose_fashion
    puts "なのでなんでもよい"
  end
end

class Context
  def initialize
    @sunny = SunnyDay.new
    @rainy = RainyDay.new
    @cloudy = CloudyDay.new
    @state = @sunny
  end
  
  def change_state(weather)
    if weather == "SunnyDay"
      @state = @sunny
    elsif weather == "RainyDay"
      @state = @rainy
    else
      @state = @cloudy
    end
  end
  
  def ice_break
    puts @state.class
    @state.ice_break
  end
  
  def choose_fashion
    @state.choose_fashion
  end
end

# Client(main)
obj = Context.new
obj.ice_break
obj.choose_fashion
puts "------" * 5
obj.change_state("RainyDay")
obj.ice_break
obj.choose_fashion
puts "------" * 5
obj.change_state("CloudyDay")
obj.ice_break
obj.choose_fashion

