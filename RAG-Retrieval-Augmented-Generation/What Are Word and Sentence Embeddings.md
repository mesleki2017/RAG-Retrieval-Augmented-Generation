https://cohere.com/llmu/sentence-word-embeddings

# Sentence embeddings

So word #embedding s seem to be pretty useful, but in reality, human language is much more complicated than simply a bunch of words put together. Human language has structure, sentences, etc. How would one be able to represent, for instance, a sentence? Well, here’s an idea. How about the sums of scores of all the words? For example, say we have a word embedding that assigns the following scores to these words:

No: [1,0,0,0]  
I: [0,2,0,0]  
Am: [-1,0,1,0]  
Good: [0,0,1,3]  
Then the sentence “No, I am good!” corresponds to the vector [0,2,2,3]. However, the sentence “I am no good” will also correspond to the vector [0,2,2,3]. This is not a good thing, since the computer understand these two sentences in the exact same way, yet they are quite different, almost opposite sentences! Therefore, we need better embeddings that take into account the order of the words, the semantics of the language, and the actual meaning of the sentence.

This is where sentence embeddings come into play. A sentence embedding is just like a word embedding, except it associates every sentence with a vector full of numbers, in a coherent way. By coherent, I mean that it satisfies similar properties as a word embedding. For instance, similar sentences are assigned to similar vectors, different sentences are assigned to different vectors, and most importantly, each of the coordinates of the #vector identifies some (whether clear or obscure) property of the sentence.
# How to Use These Embeddings?

Now that you’ve learned how useful these embeddings are, it’s time to start playing with them and finding good practical uses for them! The [Cohere dashboard](https://dashboard.cohere.ai/?ref=cohere-ai.ghost.io&__hstc=14363112.5cd142a68443e4afce0f46119d009512.1724515532866.1724515532866.1724515532866.1&__hssc=14363112.1.1724515532867&__hsfp=205995726&_gl=1*1wxn3lh*_gcl_au*MTkyODQ5NjI1NC4xNzI0NTE1NTMw) provides a very friendly interface to use them. Here is a small example, with the following phrases:

I like my dog  
I love my dog  
I adore my dog  
Hello, how are you?  
Hey, how's it going?  
Hi, what's up?  
I love watching soccer  
I enjoyed watching the world cup  
I like watching soccer matches

To see the results of the sentence embedding, go to the “Embed” tab in the Cohere dashboard, and type the sentences (click here for an embed demo you can play with)
# Conclusion

Word and sentence embeddings are the bread and butter of #LLM s. They are the basic building block of most language models, since they translate human speak (words) into computer speak (numbers) in a way that captures many relations between words, semantics, and nuances of the language, into equations regarding the corresponding numbers.

Sentence embeddings can be extended to language embeddings, in which the numbers attached to each sentence are language-agnostic. These models are very useful for translation and for searching and understanding text in different languages.