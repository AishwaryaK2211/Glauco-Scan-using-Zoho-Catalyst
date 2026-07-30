'use client';

import { motion } from 'framer-motion';
import { Eye, Activity, ShieldCheck, ArrowRight, Brain, Cpu, Zap, ChevronRight } from 'lucide-react';
import Link from 'next/link';
import { useEffect, useState } from 'react';

function ParticleField() {
  const [particles, setParticles] = useState<{ x: number; y: number; size: number; delay: number; duration: number }[]>([]);
  useEffect(() => {
    setParticles(
      Array.from({ length: 40 }, () => ({
        x: Math.random() * 100,
        y: Math.random() * 100,
        size: Math.random() * 3 + 1,
        delay: Math.random() * 5,
        duration: Math.random() * 8 + 6,
      }))
    );
  }, []);
  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none">
      {particles.map((p, i) => (
        <motion.div
          key={i}
          className="absolute rounded-full bg-electric-blue/30"
          style={{ left: `${p.x}%`, top: `${p.y}%`, width: p.size, height: p.size }}
          animate={{ y: [0, -30, 0], opacity: [0.1, 0.6, 0.1] }}
          transition={{ duration: p.duration, delay: p.delay, repeat: Infinity, ease: 'easeInOut' }}
        />
      ))}
    </div>
  );
}

function AnimatedCounter({ target, suffix = '' }: { target: number; suffix?: string }) {
  const [count, setCount] = useState(0);
  useEffect(() => {
    let start = 0;
    const inc = target / 120;
    const timer = setInterval(() => {
      start += inc;
      if (start >= target) { setCount(target); clearInterval(timer); }
      else setCount(Math.floor(start));
    }, 16);
    return () => clearInterval(timer);
  }, [target]);
  return <span>{count.toLocaleString()}{suffix}</span>;
}

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col relative overflow-hidden bg-[#05070A]">
      <ParticleField />

      {/* Ambient blobs */}
      <div className="absolute top-[-20%] left-[-15%] w-[50vw] h-[50vw] bg-electric-blue/5 rounded-full blur-[120px] pointer-events-none" />
      <div className="absolute bottom-[-20%] right-[-15%] w-[50vw] h-[50vw] bg-neon-cyan/5 rounded-full blur-[120px] pointer-events-none" />
      <div className="absolute top-[30%] right-[10%] w-[30vw] h-[30vw] bg-purple/5 rounded-full blur-[100px] pointer-events-none" />

      {/* Top bar */}
      <header className="relative z-20 flex items-center justify-between px-8 py-5">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-full bg-gradient-to-br from-neon-cyan to-electric-blue flex items-center justify-center retina-glow">
            <Eye size={18} className="text-white" />
          </div>
          <span className="text-lg font-bold tracking-wider">GLAUCOSCAN</span>
        </div>
        <nav className="flex items-center gap-6 text-sm text-gray-400">
          <a href="#features" className="hover:text-white transition-colors">Features</a>
          <a href="#pipeline" className="hover:text-white transition-colors">AI Pipeline</a>
          <Link href="/dashboard" className="px-4 py-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 text-white font-medium transition-all">
            Launch Platform
          </Link>
        </nav>
      </header>

      {/* Hero */}
      <motion.section
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1.2 }}
        className="flex-1 flex flex-col items-center justify-center text-center px-4 relative z-10 -mt-10"
      >
        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.8, ease: 'easeOut' }}
          className="mb-8 relative"
        >
          <div className="w-28 h-28 rounded-full glass-panel flex items-center justify-center retina-glow">
            <Eye size={48} className="text-neon-cyan" />
          </div>
          {/* Orbiting ring */}
          <motion.div
            className="absolute inset-[-12px] border border-neon-cyan/20 rounded-full"
            animate={{ rotate: 360 }}
            transition={{ duration: 20, repeat: Infinity, ease: 'linear' }}
          >
            <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-neon-cyan pulse-dot" />
          </motion.div>
          <motion.div
            className="absolute inset-[-24px] border border-electric-blue/10 rounded-full"
            animate={{ rotate: -360 }}
            transition={{ duration: 30, repeat: Infinity, ease: 'linear' }}
          >
            <div className="absolute bottom-0 left-1/2 -translate-x-1/2 translate-y-1/2 w-1.5 h-1.5 rounded-full bg-electric-blue" />
          </motion.div>
        </motion.div>

        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3, duration: 0.8 }}
          className="text-5xl md:text-7xl font-bold tracking-tight mb-6 max-w-4xl leading-[1.1]"
        >
          Detect Vision Loss{' '}
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-electric-blue via-neon-cyan to-purple">
            Before It&apos;s Irreversible
          </span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5, duration: 0.8 }}
          className="text-lg text-gray-400 mb-10 max-w-2xl leading-relaxed"
        >
          Enterprise-grade AI screening platform. Upload retinal fundus images and receive 
          instant Explainable AI analysis with Grad-CAM heatmaps, powered by EfficientNet-B0.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.7, duration: 0.8 }}
          className="flex flex-col sm:flex-row gap-4 mb-20"
        >
          <Link href="/dashboard">
            <motion.button
              whileHover={{ scale: 1.03, boxShadow: '0 0 30px rgba(0, 229, 255, 0.3)' }}
              whileTap={{ scale: 0.97 }}
              className="px-8 py-4 bg-gradient-to-r from-electric-blue to-neon-cyan text-black rounded-xl font-bold tracking-wide flex items-center gap-2 text-sm"
            >
              Open Command Center <ArrowRight size={18} />
            </motion.button>
          </Link>
          <motion.button
            whileHover={{ scale: 1.03 }}
            whileTap={{ scale: 0.97 }}
            className="px-8 py-4 glass-panel text-white rounded-xl font-semibold tracking-wide flex items-center gap-2 text-sm hover:border-white/20"
          >
            View API Docs <ChevronRight size={16} />
          </motion.button>
        </motion.div>

        {/* Stats ticker */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
          className="flex items-center gap-8 text-center mb-12"
        >
          {[
            { value: 1247, label: 'Scans Processed', suffix: '+' },
            { value: 94, label: 'AI Accuracy', suffix: '%' },
            { value: 850, label: 'Risk Detected', suffix: '+' },
            { value: 12, label: 'Hospitals', suffix: '' },
          ].map((stat, i) => (
            <div key={i} className="px-6">
              <p className="text-2xl md:text-3xl font-bold font-mono text-white counter-glow">
                <AnimatedCounter target={stat.value} suffix={stat.suffix} />
              </p>
              <p className="text-[10px] uppercase tracking-widest text-gray-500 mt-1">{stat.label}</p>
            </div>
          ))}
        </motion.div>
      </motion.section>

      {/* Feature Grid */}
      <section id="features" className="relative z-10 max-w-6xl mx-auto px-4 pb-20 w-full">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { icon: <Brain className="text-electric-blue" size={22} />, title: 'EfficientNet-B0 AI', desc: 'Transfer-learned deep neural network trained on diverse retinal datasets with CLAHE preprocessing and real-time inference.' },
            { icon: <Eye className="text-neon-cyan" size={22} />, title: 'Grad-CAM Explainability', desc: 'Visual attention heatmaps highlight the exact optic disc and cup regions influencing each prediction.' },
            { icon: <ShieldCheck className="text-purple" size={22} />, title: 'Hospital-Grade Reports', desc: 'WeasyPrint PDF reports with annotated retinal images, CDR estimation, risk gauges, and clinical recommendations.' },
            { icon: <Activity className="text-green-400" size={22} />, title: 'Real-Time Analytics', desc: 'Interactive dashboards with risk distribution trends, CDR progression, confidence tracking, and screening statistics.' },
            { icon: <Cpu className="text-amber-400" size={22} />, title: 'FastAPI Backend', desc: 'Production-grade async Python backend with SQLAlchemy ORM, JWT auth, and modular adapter architecture.' },
            { icon: <Zap className="text-pink-400" size={22} />, title: 'Catalyst-Ready', desc: 'Adapter patterns for Storage, Auth, and Database ensure seamless future migration to Zoho Catalyst.' },
          ].map((feature, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.08 }}
              className="glass-panel-hover p-5 rounded-xl"
            >
              <div className="mb-3 p-2.5 rounded-lg bg-white/5 inline-flex">{feature.icon}</div>
              <h3 className="text-sm font-bold text-white mb-2">{feature.title}</h3>
              <p className="text-xs text-gray-400 leading-relaxed">{feature.desc}</p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="relative z-10 border-t border-[#142240] py-6 text-center">
        <p className="text-[10px] text-gray-600 uppercase tracking-widest">
          GlaucoScan Vision Intelligence Platform — EfficientNet-B0 · Grad-CAM · FastAPI · Next.js
        </p>
      </footer>
    </div>
  );
}
