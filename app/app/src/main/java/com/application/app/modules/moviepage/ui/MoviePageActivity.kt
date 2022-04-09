package com.application.app.modules.moviepage.ui

import androidx.activity.viewModels
import com.application.app.R
import com.application.app.appcomponents.base.BaseActivity
import com.application.app.databinding.ActivityMoviePageBinding
import com.application.app.modules.moviepage.`data`.viewmodel.MoviePageVM
import kotlin.String
import kotlin.Unit

public class MoviePageActivity :
    BaseActivity<ActivityMoviePageBinding>(R.layout.activity_movie_page) {
  private val viewModel: MoviePageVM by viewModels<MoviePageVM>()

  public override fun onInitialized(): Unit {
    viewModel.navArguments = intent.extras?.getBundle("bundle")
    binding.moviePageVM = viewModel
  }

  public override fun setUpClicks(): Unit {
  }

  public companion object {
    public const val TAG: String = "MOVIE_PAGE_ACTIVITY"
  }
}
