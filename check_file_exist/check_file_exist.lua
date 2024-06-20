local file_path = "./a.txt"
local file = io.open(file_path, "r")

-- todo verify
-- run cmd: lua check_file_exist.lua
if file then
    print(file_path .. " exists.")
    file:close()
else
    print(file_path .. " does not exist.")
end
