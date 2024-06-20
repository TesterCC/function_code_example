file = "./a.txt"

# ruby check_file_exist.rb
if File.exist?(file)
  puts "#{file} exists."
else
  puts "#{file} does not exist."
end
