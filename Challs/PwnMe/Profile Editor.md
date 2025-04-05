```python
@app.route('/show_profile', methods=['GET', 'POST'])
def show_profile():
    if not session.get('username'):
        return redirect('/login')
    
    profiles_file = 'profile/' + session.get('username')

    if commonpath((app.root_path, abspath(profiles_file))) != app.root_path:
        return render_template('error.html', msg='Error processing profile file!', return_to='/profile')

    profile = ''
    if exists(profiles_file):
        with open(profiles_file, 'r') as f:
            profile = f.read()

    return render_template('show_profile.html', username=session.get('username'), profile=profile)
```

username : `../flag.txt`

Then /show_profile gives the flag