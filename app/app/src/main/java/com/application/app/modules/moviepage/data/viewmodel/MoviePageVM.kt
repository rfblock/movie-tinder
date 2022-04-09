package com.application.app.modules.moviepage.`data`.viewmodel

import android.os.Bundle
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.application.app.modules.moviepage.`data`.model.MoviePageModel
import org.koin.core.KoinComponent

public class MoviePageVM : ViewModel(), KoinComponent {
  public val moviePageModel: MutableLiveData<MoviePageModel> = MutableLiveData(MoviePageModel())

  public var navArguments: Bundle? = null
}
