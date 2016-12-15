gulp = require 'gulp'
cssmin = require 'gulp-cssmin'
compass = require 'gulp-compass'
merge = require 'merge2'
browserify = require 'browserify'
source = require 'vinyl-source-stream'

gulp.task 'styles', ->
  stream1 = gulp.src 'assets/styles/*.css'
    .pipe cssmin()
    .pipe gulp.dest 'public/styles'
  stream2 = gulp.src 'assets/styles/*.scss'
    .pipe compass
      project: __dirname
      sass: 'assets/styles'
      css: 'css'
      import_path: [ 'node_modules' ]
      style: 'expanded' # or compressed
      sourcemap: true
  merge stream1, stream2

gulp.task 'scripts', ->
  browserify
    entries: ['./assets/scripts/main.coffee']
    extentions: ['.coffee']
  .bundle()
  .pipe source 'main.js'
  .pipe gulp.dest 'js'

gulp.task 'watch', ->
  gulp.watch 'assets/styles/**', ['styles']
  gulp.watch 'assets/scripts/**', ['scripts']

gulp.task 'default', [ 'styles', 'scripts', 'watch' ]

