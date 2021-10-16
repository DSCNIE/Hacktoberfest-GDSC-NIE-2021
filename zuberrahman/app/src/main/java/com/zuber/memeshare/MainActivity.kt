package com.zuber.memeshare

import android.content.Intent
import android.graphics.drawable.Drawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.ProgressBar
import android.widget.Toast
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.JsonObjectRequest
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.bumptech.glide.Glide
import com.bumptech.glide.load.DataSource
import com.bumptech.glide.load.engine.GlideException
import com.bumptech.glide.request.RequestListener
import com.bumptech.glide.request.target.Target

class MainActivity : AppCompatActivity() {

     lateinit var ShareButton : Button
     lateinit var NextButton : Button
    lateinit var MemeImageView : ImageView
     lateinit var Progressbar : ProgressBar
     var currentImageUrl : String? = null



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        ShareButton = findViewById(R.id.shareMeme)
        NextButton = findViewById(R.id.nextMeme)
        MemeImageView = findViewById(R.id.memeImageView)
        Progressbar = findViewById(R.id.progressBar)

        Progressbar.visibility = View.VISIBLE

        loadMeme()





        ShareButton.setOnClickListener{

            val intent = Intent(Intent.ACTION_SEND)
            intent.type = "text/plain"
            intent.putExtra(Intent.EXTRA_TEXT,"$currentImageUrl")
            val chooser = Intent.createChooser(intent,"Send this using")
            startActivity(chooser)
        }

        NextButton.setOnClickListener{

            loadMeme()


        }


    }

    private fun loadMeme(){
        Progressbar.visibility = View.VISIBLE
        val queue = Volley.newRequestQueue(this)
        val url = "https://meme-api.herokuapp.com/gimme"

// Request a string response from the provided URL.
        val stringRequest = JsonObjectRequest(
            Request.Method.GET, url,null,
            { response ->
                val currentImageUrl = response.getString("url")
                Glide.with(this).load(currentImageUrl).listener(object : RequestListener<Drawable>{
                    override fun onLoadFailed(
                        e: GlideException?,
                        model: Any?,
                        target: Target<Drawable>?,
                        isFirstResource: Boolean
                    ): Boolean {
                        Progressbar.visibility = View.GONE
                        return false
                    }

                    override fun onResourceReady(
                        resource: Drawable?,
                        model: Any?,
                        target: Target<Drawable>?,
                        dataSource: DataSource?,
                        isFirstResource: Boolean
                    ): Boolean {
                        Progressbar.visibility = View.GONE
                        return false
                    }

                }).into(MemeImageView)


            },
            {
                Toast.makeText(this, "Error Occured", Toast.LENGTH_SHORT).show()
            })


// Add the request to the RequestQueue.
        queue.add(stringRequest)
    }


}