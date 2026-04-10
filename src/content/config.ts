import { defineCollection, z } from 'astro:content';

const pasantiasCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.string(),
    readingTime: z.string(),
  }),
});

export const collections = {
  pasantias: pasantiasCollection,
};
