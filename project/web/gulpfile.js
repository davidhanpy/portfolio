var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');
var concatCSS = require('gulp-concat-css');

gulp.task('css', function() {
	gulp.src('static/css/src/*.css')
  .pipe(concatCSS('bundle.css'))
  .pipe(cleanCSS())
	.pipe(gulp.dest('static/css'));
});

gulp.task('watch',function() {
	gulp.watch('static/css/src/*.css',['css']);
});

gulp.task('default',['css','watch']); 