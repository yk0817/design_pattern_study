require 'fileutils'

# 参考
# http://morizyun.github.io/ruby/design-pattern-command.html


class Command
  attr_reader :description
  def initialize(description)
    @description = description
  end
  
  def execute
  end
  
  def undo_execute
  end
end


class CreateFile < Command
  def initialize(path,contents)
    super("Create file : #{path}")
    @path = path
    @contents = contents
  end
  
  def execute
    f = File.open(@path,"w")
    f.write(@contents)
    f.close
  end
  
  def undo_execute
    File.delete(@path)
  end
end

class DeleteFile < Command
  def initialize(path)
    super("Delete file:#{path}")
  end
  
  def execute
    if File.exists?(@path)
      @content = File.read(@path)
    end
    File.delte(@path)
  end
  
  def undo_execute
    f = File.open(@path,"w")
    f.write(@contents)
    f.close
  end
end

class CopyFile < Command
  def initialize(source,target)
    super("copy file: #{source} to #{target}")
    @source = source
    @target = target
  end
  
  def execute
    FileUtils.copy(@source,@target)
  end
  
  def undo_execute
    File.delete(@target)
    if @contents
      f = File.open(@target,"w")
      f.write(@contents)
      f.close
    end
  end
end

class CompositeCommand < Command
  def initialize
    @commands = []
  end
  
  def add_command(cmd)
    @commands << cmd
  end
  def execute
    @commands.each do |cmd|
      cmd.execute
    end
  end
  
  def undo_execute
    @commands.reverse.each do |cmd|
      cmd.undo_execute
    end
  end
  
  def description
    description = ""
    @commands.each do |cmd|
      description += cmd.description + "\n"
    end
  end
end

command_list = CompositeCommand.new
command_list.add_command(CreateFile.new("file1.txt","helloworld\n"))
command_list.add_command(CopyFile.new("file1.txt","file2.txt"))
command_list.add_command(DeleteFile.new("file1.txt"))


