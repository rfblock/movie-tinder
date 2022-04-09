package com.application.app.modules.moviepage.`data`.model

import com.application.app.R
import com.application.app.appcomponents.di.MyApp
import kotlin.String

public data class MoviePageModel(
  /**
   * TODO Replace with dynamic value
   */
  public var txtHereIsWhereY: String? =
      MyApp.getInstance().resources.getString(R.string.msg_here_is_where_y)
  ,
  /**
   * TODO Replace with dynamic value
   */
  public var txtSPIDERMANFA: String? =
      MyApp.getInstance().resources.getString(R.string.msg_spider_man_fa)
  ,
  /**
   * TODO Replace with dynamic value
   */
  public var txtSuscipitTellus: String? =
      MyApp.getInstance().resources.getString(R.string.msg_suscipit_tellus)
  ,
  /**
   * TODO Replace with dynamic value
   */
  public var txtMoreInfo: String? = MyApp.getInstance().resources.getString(R.string.lbl_more_info)
  ,
  /**
   * TODO Replace with dynamic value
   */
  public var txtRecomendations: String? =
      MyApp.getInstance().resources.getString(R.string.lbl_recomendations)

)
