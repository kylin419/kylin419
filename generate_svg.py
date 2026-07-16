import datetime

# ASCII Art provided by the user
ascii_art = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@ . .   .  -+*+***@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@*=              -+*========#%@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                   -+*+==+*********@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@:         .   .       -+*++++=======----+@@@@@@@@@@@@@@@
@@@@@@@@@@@@@   . .    .              ====------+***::::::@@@@@@@@@@@@@
@@@@@@@@@@%        .     .   .      .::====:::::=========::-@@@@@@@@@@@
@@@@@@@@@                     .=+++++++++++:+++++++++::-- .   @@@@@@@@@
@@@@@@@@.     .          .----=++++++++++++.+++++++++::- . ..  %@@@@@@@
@@@@@@: ....:++++++++===+--=-.:+++++++#****-****+++++:::  .  .   @@@@@@
@@@@@..+++++=-++++--=:-.+.-::..=+++#@+=-=++++==+#@#++:::...       @@@@@
@@@@* :++++++=-=-=::---=+==++++++*#==******#%##*+-*@+:::....  .    %@@@
@@@@*.:++++++++=+**+------------+*=***#%%%%%%%%%**+-%:::..         =@@@
@@%*:.-+=::::...............:-.+@-**##%%%%%%%%%%%%*+*-::           .*@@
@@**::-+-..::**:=*******.::*@@#-=%%%%%%%%%%%%%%%%%#*=@::       .    :@@
@###::-+-.:**+***====:*#%%##++++****#%%@@@%%%%%%%%%*=@:.            .=@
@+**:--+:....-++**+++:..@@@@@@***#%%%%%%%%%@@@%%%%#+=@:.              #
@*##--=#-...**------=*+.:-====+@@@@@@@@%%##%@@@@*==#*@:.          .   #
++**--=#-:::++-:::::-+=:::::::::@########**#%@%=*++@@-:.           .   
++**=-=#-:::::::::::::::::::--=+#@+####*==--*%+=#=#@#.::  ..   .      .
++**=-*#-:-+##+##+#++#*+:::+=#=***-++=----=====+*=*@+.:.      .        
****=-*#-::+**###*###**=::--+*+:-##*+=--======-==-..*.:.     .   .     
++**=-*#-:::===+##+====:::*#+:+=*:**=========-++==-.=-+-               
@+**=-*#-:--=##*##*##=-=::***-*#-::**+======*##====-:.:%%+. .   .     *
@***=-*#-::-=-:-==-::-==::-=##-=*--%@==+#####*=======--***#@.   . .   #
@#**=-*+-::::::-=-::::::::+++#%##:       +*+**+=====+#@@@%*   :*. .  :@
@@**=-*+-:-*****#*:::::::::*#.        .  .-#%*+++###@@@@#-.....   @- %@
@@%+--*+-:-##--=#*---*#=:::%... .   ....:..-----==@@@@%++=--:::::. :@@@
@@@%--*+-:-##*####**###=::@. .       . ....----=%@@@%++++++=++++=-.+@@@
@@@@=-*+-:::---=#*---=+-:+.  ..  .       ...--#@@@@+==+++=====+==--@@@@
@@@@@=*+-:::::-=**::::--:*   .      .  ....-=%@@@*=-----=++++++-==@@@@@
@@@@@@*##*******=-====-:@    ..      -...:-#@@@@+----------=-==-+@@@@@@
@@@@@@@@+++++*+++++++*### .. .  .  .-..:--#@@@*---------------=@@@@@@@@
@@@@@@@@@####%%%%%*%*#%@ ... ...  -:..--*@@@@+:-------###++---@@@@@@@@@
@@@@@@@@@@@##++*######%-........ .-:--=%@@@@-.:----------=++@@@@@@@@@@@
@@@@@@@@@@@@@+++++++++% ...-..:  ----+@@@@*:.:----------::%@@@@@@@@@@@@
@@@@@@@@@@@@@@@#+++++@ ....::.: ----*@@@@-.:---.:------+@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@%+*:......-. :---#@@@@-.---:.:----*@@@@@@@@@@@@@%*@@@
@@@@@@@@@@@@@@@@@@@@@#+..:.:--.---%@@@*----:..:-*#@@@@@@@@@@@@@@@@@#@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@-== -=%@@@+--::--@@@@@@@@@@@@@@@@@@@@@@@@@@@
""".strip().split('\n')

# Width settings
ASCII_CHAR_WIDTH = 71
ASCII_START_X = 15
STATS_START_X = 640 # Shift stats to the left
SVG_WIDTH = 1550 # Widen the card to prevent truncation
SVG_HEIGHT = 830

# Calculate Uptime
start_date = datetime.date(2021, 11, 29)
today = datetime.date.today()
diff = today - start_date
years = diff.days // 365
months = (diff.days % 365) // 30
days = (diff.days % 365) % 30
uptime_str = f"{years} years, {months} months, {days} days"

# Stats definitions
# Format: (type, label/prefix, value/suffix)
stats_data = [
    ('header', 'kylin419@github', ''),
    ('item', 'OS', 'macOS'),
    ('item', 'Uptime', uptime_str),
    ('item', 'Host', 'National Kaohsiung University of Science and Technology'),
    ('item', 'Kernel', '電子工程系資訊組 (Electronic Engineering - CS Track)'),
    ('item', 'IDE', 'VSCode, JetBrains'),
    ('empty',),
    ('item', 'Languages.Programming', 'Go, Rust, Python, C++, C, Java, PHP, Verilog'),
    ('item', 'Languages.Web', 'HTML, CSS, React, Next.js, Node.js, Express'),
    ('empty',),
    ('item', 'Hobbies.Software', 'CVForge, Lingo, YOLO PCB Defect Detection'),
    ('item', 'Hobbies.Hardware', 'STM32, ESP32, Arduino, DE2-115'),
    ('empty',),
    ('contact-header', '- Contact', ''),
    ('item', 'GitHub', 'github.com/kylin419'),
    ('item', 'Website', 'https://kylindev.me'),
    ('item', 'Discord', 'kylin419'),
    ('item', 'LinkedIn', '/in/your-linkedin'),
    ('empty',),
    ('stats-header', '- GitHub Stats', ''),
    ('stats-git', 'Repos', '18', '5', '5'), # (Repos, Contributed, Stars)
    ('stats-commits', 'Commits', '250', '5'), # (Commits, Followers)
    ('stats-loc', 'Lines of Code', '45,210', '52,170', '6,960'), # (LOC, Additions, Deletions)
]

def generate_svg():
    svg_lines = []
    svg_lines.append("<?xml version='1.0' encoding='UTF-8'?>")
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="{SVG_WIDTH}px" height="{SVG_HEIGHT}px" font-size="15px">')
    svg_lines.append('<style>')
    svg_lines.append('  @font-face {')
    svg_lines.append("    src: local('Consolas'), local('Consolas Bold');")
    svg_lines.append("    font-family: 'ConsolasFallback';")
    svg_lines.append('    font-display: swap;')
    svg_lines.append('    -webkit-size-adjust: 109%;')
    svg_lines.append('    size-adjust: 109%;')
    svg_lines.append('  }')
    svg_lines.append('  .key {fill: #ffa657;}')
    svg_lines.append('  .value {fill: #a5d6ff;}')
    svg_lines.append('  .addColor {fill: #3fb950;}')
    svg_lines.append('  .delColor {fill: #f85149;}')
    svg_lines.append('  .cc {fill: #616e7f;}')
    svg_lines.append('  text, tspan {white-space: pre;}')
    svg_lines.append('</style>')
    
    # Background card
    svg_lines.append(f'<rect width="{SVG_WIDTH}px" height="{SVG_HEIGHT}px" fill="#161b22" rx="15"/>')
    
    # ASCII Art block
    svg_lines.append('<!-- ASCII Art -->')
    svg_lines.append(f'<text x="{ASCII_START_X}" y="35" fill="#c9d1d9" class="ascii">')
    for i, line in enumerate(ascii_art):
        y_pos = 35 + i * 20
        # Escape XML chars in ASCII
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        svg_lines.append(f'  <tspan x="{ASCII_START_X}" y="{y_pos}">{escaped_line}</tspan>')
    svg_lines.append('</text>')
    
    # Stats block
    svg_lines.append('<!-- Stats -->')
    svg_lines.append(f'<text x="{STATS_START_X}" y="35" fill="#c9d1d9">')
    
    current_y = 35
    for row in stats_data:
        t = row[0]
        if t == 'empty':
            svg_lines.append(f'  <tspan x="{STATS_START_X}" y="{current_y}"> </tspan>')
            current_y += 20
            continue
            
        if t == 'header':
            label = row[1]
            dash_len = 70 # characters of dashes (increased from 35)
            dashes = "-" * dash_len
            svg_lines.append(f'  <tspan x="{STATS_START_X}" y="{current_y}">{label}</tspan> <tspan class="cc">{dashes}</tspan>')
            current_y += 20
            continue
            
        if t == 'contact-header' or t == 'stats-header':
            label = row[1]
            dash_len = 77 # characters of dashes (increased from 42)
            dashes = "-" * dash_len
            svg_lines.append(f'  <tspan x="{STATS_START_X}" y="{current_y}">{label}</tspan> <tspan class="cc">{dashes}</tspan>')
            current_y += 20
            continue
            
        if t == 'item':
            key = row[1]
            val = row[2]
            
            # Align dots
            # We want key + dots to be around 28 characters
            parts = key.split('.')
            key_xml = ""
            if len(parts) > 1:
                key_xml = f'<tspan class="key">{parts[0]}</tspan>.<tspan class="key">{parts[1]}</tspan>'
            else:
                key_xml = f'<tspan class="key">{key}</tspan>'
                
            dot_count = 28 - len(key)
            if dot_count < 2:
                dot_count = 2
            dots = "." * dot_count
            
            svg_lines.append(f'  <tspan x="{STATS_START_X}" y="{current_y}" class="cc">. </tspan>{key_xml}:<tspan class="cc"> {dots} </tspan><tspan class="value">{val}</tspan>')
            current_y += 20
            continue
            
        if t == 'stats-git':
            key = row[1]
            repo_val = row[2]
            contrib_val = row[3]
            star_val = row[4]
            
            # Key (Repos) + dots
            dot_count_repos = 6 - len(key)
            dots_repos = "." * dot_count_repos
            
            # Stars + dots
            dot_count_stars = 12
            dots_stars = "." * dot_count_stars
            
            line_str = (
                f'  <tspan x="{STATS_START_X}" y="{current_y}" class="cc">. </tspan>'
                f'<tspan class="key">{key}</tspan>:<tspan class="cc"> {dots_repos} </tspan>'
                f'<tspan class="value">{repo_val}</tspan> '
                f'{{<tspan class="key">Contributed</tspan>: <tspan class="value">{contrib_val}</tspan>}} | '
                f'<tspan class="key">Stars</tspan>:<tspan class="cc"> {dots_stars} </tspan>'
                f'<tspan class="value">{star_val}</tspan>'
            )
            svg_lines.append(line_str)
            current_y += 20
            continue
            
        if t == 'stats-commits':
            key = row[1]
            commit_val = row[2]
            follower_val = row[3]
            
            dot_count_commits = 20 - len(key)
            dots_commits = "." * dot_count_commits
            
            dot_count_followers = 8
            dots_followers = "." * dot_count_followers
            
            line_str = (
                f'  <tspan x="{STATS_START_X}" y="{current_y}" class="cc">. </tspan>'
                f'<tspan class="key">{key}</tspan>:<tspan class="cc"> {dots_commits} </tspan>'
                f'<tspan class="value">{commit_val}</tspan> | '
                f'<tspan class="key">Followers</tspan>:<tspan class="cc"> {dots_followers} </tspan>'
                f'<tspan class="value">{follower_val}</tspan>'
            )
            svg_lines.append(line_str)
            current_y += 20
            continue
            
        if t == 'stats-loc':
            key = row[1]
            loc_val = row[2]
            add_val = row[3]
            del_val = row[4]
            
            dot_count_loc = 1
            dots_loc = "." * dot_count_loc
            
            line_str = (
                f'  <tspan x="{STATS_START_X}" y="{current_y}" class="cc">. </tspan>'
                f'<tspan class="key">{key}</tspan>:<tspan class="cc"> {dots_loc} </tspan>'
                f'<tspan class="value">{loc_val}</tspan> '
                f'( <tspan class="addColor">{add_val}</tspan><tspan class="addColor">++</tspan>, '
                f'<tspan class="delColor">{del_val}</tspan><tspan class="delColor">--</tspan> )'
            )
            svg_lines.append(line_str)
            current_y += 20
            continue
            
    svg_lines.append('</text>')
    svg_lines.append('</svg>')
    
    with open('profile_card.svg', 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print("profile_card.svg generated successfully.")

if __name__ == '__main__':
    generate_svg()
